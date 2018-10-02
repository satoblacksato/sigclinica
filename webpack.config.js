var path = require('path')
var webpack = require('webpack')

module.exports = {
    entry: {
        empleados: './static/apps/empleados/empleados.js',
        pacientes: './static/apps/pacientes/pacientes.js',
        turnos: './static/apps/turnos/turnos.js',
        tipoDocumento: './static/apps/complementos/tipoDocumento/tipoDocumento.js',
        obraSocial: './static/apps/complementos/obraSocial/obraSocial.js',
        chat: './static/apps/chat/chat.js',
        ventanaChat: './static/apps/ventanaChat/ventanaChat.js',
        nota: './static/apps/notas/nota.js',
        fichasClinicas: './static/apps/fichasClinicas/fichasClinicas.js'
    },
    output: {
        path: path.resolve(__dirname, './static/apps-compiler/'),
        publicPath: '/static/apps-compiler/',
        filename: "[name].js"
    },
    module: {
        rules: [{
                test: /\.vue$/,
                loader: 'vue-loader',
                options: {
                    loaders: {}
                    // other vue-loader options go here
                }
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/
            },
            {
                test: /\.(png|jpg|gif|svg)$/,
                loader: 'file-loader',
                options: {
                    name: '[name].[ext]?[hash]'
                }
            }
        ]
    },
    plugins: [],
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.esm.js'
        }
    },
    devServer: {
        historyApiFallback: true,
        noInfo: true
    },
    performance: {
        hints: false
    },
    devtool: '#eval-source-map'
}

if (process.env.NODE_ENV === 'production') {
    module.exports.devtool = '#source-map'
        // http://vue-loader.vuejs.org/en/workflow/production.html
    module.exports.plugins = (module.exports.plugins || []).concat([
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: '"production"'
            }
        }),
        new webpack.optimize.UglifyJsPlugin({
            sourceMap: true,
            compress: {
                warnings: false
            }
        }),
        new webpack.LoaderOptionsPlugin({
            minimize: true
        })
    ])
}