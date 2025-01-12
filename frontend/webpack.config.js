module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
      test: /\.css$/,
      exclude: /node_modules/,
      loader: 'css-loader',
      },
    ]
  }
};