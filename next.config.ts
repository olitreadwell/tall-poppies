import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  basePath: process.env.BASE_PATH ?? undefined,
  output: process.env.DOCKER_BUILD === '1' ? 'standalone' : undefined,
  reactStrictMode: true,
  allowedDevOrigins: ['127.0.0.1'],
};

export default nextConfig;
