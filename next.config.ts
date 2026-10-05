import type { NextConfig } from 'next';
const config: NextConfig = {
  basePath: '/labs/datasenter-analyse-norge',
  transpilePackages: ['mapbox-gl'],
  serverExternalPackages: ['apache-arrow'],
  poweredByHeader: false,
};
export default config;
