import CssMinimizerPlugin from 'css-minimizer-webpack-plugin';
import { mergeWithRules } from 'webpack-merge';
import common from './webpack.common.mjs';

const mergeRules = Object.freeze({
    mode: 'replace',
});

const CssMinimizerConfig = Object.freeze({
    parallel: true,
    minimizerOptions: {
        preset: 'advanced',
    },
});

export default mergeWithRules(mergeRules)(common, {
    mode: 'production',

    optimization: {
        mangleExports: 'size',
        minimize: true,
        minimizer: [
            '...',
            new CssMinimizerPlugin(CssMinimizerConfig),
        ],
    },
});
