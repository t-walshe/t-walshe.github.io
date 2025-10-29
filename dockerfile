# Dockerfile
FROM ruby:3.3-bookworm

# System deps for native gems & timezones
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends build-essential nodejs tzdata && \
    rm -rf /var/lib/apt/lists/*

# Set your local timezone so "future" vs "past" matches your expectations
ENV TZ=Europe/London

WORKDIR /site

# Install gems first (cached layer)
COPY Gemfile* ./
RUN gem install bundler:2 && \
    bundle config set path 'vendor/bundle' && \
    bundle install || true

# Then add the rest of the project
COPY . .

# Expose Jekyll + LiveReload
EXPOSE 4000 35729

# Default command is dev-friendly; prod will override via compose profile
CMD ["bundle", "exec", "jekyll", "serve", \
     "--host", "0.0.0.0", "--port", "4000", \
     "--livereload", "--incremental", "--force_polling", \
     "--drafts", "--future"]