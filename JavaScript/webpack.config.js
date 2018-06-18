const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');

const config = {
	mode: 'development',
	entry: {
		game: './src/game.js'
	},
	module: {
		rules: [
			{ test: /\.jsx?$/, use: 'babel-loader' },
			{ test: /\.css$/, use: ['style-loader', 'css-loader'] },
			{ test: /\.(png|jpg|jpeg|gif|svg)/, use: ['file-loader'] }
		]
	},
	devServer: {
		contentBase: './dist',
		// hot: true
	},
	plugins: [
		new HtmlWebpackPlugin({
			title: 'Shoot-Em Up!',
			minify: true,
			hash: true,
			inject: false,
			template: require('html-webpack-template'),
			appMountId: 'app'
		})
	],
	output: {
		filename: '[name].bundle.js',
		path: path.resolve(__dirname, 'dist')
	}
};

module.exports = config;