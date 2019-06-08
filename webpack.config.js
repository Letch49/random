const webpack = require('webpack');
const path = require('path');

module.exports = {
  mode: 'development',
  entry: {
    main: ['./src/js/main.js']
  },
  output: {
    filename: "[name].js",
    path: path.resolve(__dirname, './istd/static/dist'),
    library: ['main'],
  },
  watchOptions: {
    aggregateTimeout: 100
  },
  devServer: {
    contentBase: path.join(__dirname, ''),
    compress: true,
    hot: true,
    https: false,
    host: '10.193.27.8',
    port: '80',
    hot: true
  },
}