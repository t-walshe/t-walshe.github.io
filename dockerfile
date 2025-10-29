# Use a multi-arch Ruby base (works on Apple Silicon and Intel)
FROM ruby:3.3-bookworm

# Install build tools (for native gems) and Node (for asset pipelines if used)
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends build-essential nodejs && \
    rm -rf /var/lib/apt/lists/*

# Workdir inside the container
WORKDIR /site

# Install gems first (cached by Docker layer)
# Copy only Gemfile(s) first to maximize cache hits
COPY Gemfile* ./
RUN gem install bundler:2 && \
    bundle config set path 'vendor/bundle' && \
    bundle install || true
# The '|| true' lets this succeed even if no Gemfile.lock exists yet

# Now bring in the rest of the project
COPY . .

# Expose Jekyll dev server and LiveReload ports
EXPOSE 4000 35729

# Use force_polling so file changes on macOS bind mounts are detected
CMD ["bundle", "exec", "jekyll", "serve", \
     "--host", "0.0.0.0", "--port", "4000", \
     "--livereload", "--incremental", "--force_polling"]