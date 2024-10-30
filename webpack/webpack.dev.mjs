import ESLintPlugin from 'eslint-webpack-plugin';
import { mergeWithRules } from 'webpack-merge';
import webpack from 'webpack';

import common from './webpack.common.mjs';

const mergeRules = Object.freeze({
    mode: 'replace',
    plugins: 'prepend',
});

const ESLintConfig = Object.freeze({
    configType: 'flat',
    extensions: ['ts'],
    failOnError: false,
});

export default mergeWithRules(mergeRules)(common, {
    mode: 'development',
    devtool: 'source-map',

    plugins: [
        new webpack.ProgressPlugin(), 
        new ESLintPlugin(ESLintConfig)
    ],
});
