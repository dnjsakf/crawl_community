const path = require('path');
const webpack = require('webpack');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  name: 'flask',
  mode: 'development',
  node: {
    fs: 'empty'
  },
  devtool: 'eval',
  resolve: {
    extensions: ['.js', '.jsx'],
  },
  entry: [
    './client/index.js'
  ],
  output: {
    path: path.join(__dirname, 'dist'),
    filename: 'app.js',
    publicPath: '/dist',
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        loader: 'babel-loader',
        options: {
          presets: [
            ['@babel/preset-env', {
              targets: { browsers: ['last 2 chrome versions'] },
              debug: true,
            }],
            '@babel/preset-react',
          ],
          plugins: [
            'react-hot-loader/babel',
            '@babel/plugin-proposal-class-properties',
          ],
        },
        exclude: path.join(__dirname, 'node_modules'),
      },
      {
        loader: 'file-loader',
        exclude: [/\.(js|mjs|jsx|ts|tsx)$/, /\.html$/, /\.json$/],
        options: {
          name: '/static/[name].[ext]',
        },
      },
      {
        test: [/\.bmp$/, /\.gif$/, /\.jpe?g$/, /\.png$/],
        loader: 'url-loader',
        options: {
          limit: 10000,
          name: '/static/[name].[ext]',
        },
      },
      {
        test: [/\.css$/],
        use: [ MiniCssExtractPlugin.loader, 'css-loader' ],
      }
    ],
  },
  plugins:[
    new MiniCssExtractPlugin({ filename: 'app.css' })
    , new HtmlWebpackPlugin({
      template: 'client/static/index.html'
    })
  ],
  resolve: {
    alias: {
      Components: path.resolve( __dirname, 'client/components')
    }
  },
  devServer: {
    host: 'localhost',
    port: 4000,
    historyApiFallback: true,
    hot: true,
    contentBase: path.join(__dirname,'client/static')
  },
};