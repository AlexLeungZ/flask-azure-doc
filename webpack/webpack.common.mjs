import MiniCssExtractPlugin from 'mini-css-extract-plugin';
import RemoveEmptyScriptsPlugin from 'webpack-remove-empty-scripts';

import { resolve } from 'path';

const MCEConfig = Object.freeze({
    filename: 'css/[name].css',
});

export default {
    entry: {
        script: './webapp/script/script.ts',
        style: [
            './webapp/sass/style.sass',
            './webapp/sass/tailwind.sass',
        ],
    },

    module: {
        rules: [
            {
                test: /\.([cm]?ts|tsx)$/,
                use: [
                    'ts-loader',
                    //
                ],
                exclude: /node_modules/,
            },
            {
                test: /\.(sa|sc)ss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    'postcss-loader',
                    'sass-loader',
                    //
                ],
            },
        ],
    },

    resolve: {
        extensions: [
            '.tsx',
            '.ts',
            '.js',
            //
        ],
    },

    output: {
        path: resolve('webapp', 'static'),
        filename: 'js/[name].js',
        clean: {
            keep: /ico\//,
        },
    },

    plugins: [
        new RemoveEmptyScriptsPlugin(), 
        new MiniCssExtractPlugin(MCEConfig),
    ],
};
