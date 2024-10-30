import { FlatCompat } from '@eslint/eslintrc';
import eslint from '@eslint/js';
import tsParser from '@typescript-eslint/parser';
import eslintPrettier from 'eslint-config-prettier';
import eslintPrettierRecommended from 'eslint-plugin-prettier/recommended';
import tseslint from 'typescript-eslint';
import tailwind from "eslint-plugin-tailwindcss";

import globals from 'globals';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const compat = new FlatCompat({
    baseDirectory: __dirname,
});

export default [
    {
        ignores: [
            'temp',
            'backup',
            'deploy',
            'webpack',
            'webapp/static',
            '**/node_modules',
            '**/eslint.config.*',
            '**/postcss.config.*',
            '**/tailwind.config.*',
            '**/.prettierrc.*',
        ],
    },
    ...compat.extends(),
    eslint.configs.recommended,
    ...tseslint.configs.recommendedTypeChecked,
    ...tseslint.configs.stylisticTypeChecked,
    ...tailwind.configs['flat/recommended'],
    eslintPrettierRecommended,
    eslintPrettier,
    {
        languageOptions: {
            globals: {
                ...globals.browser,
            },

            parser: tsParser,
            ecmaVersion: 'latest',
            sourceType: 'module',

            parserOptions: {
                projectService: true,
                tsconfigRootDir: import.meta.dirname,
            },
        },

        rules: {
            indent: 'error',
            camelcase: 'error',
            'prefer-const': 'error',
            'prettier/prettier': 'error',
            'no-duplicate-imports': 'error',
            'no-useless-computed-key': 'error',
            'no-useless-constructor': 'error',
            'no-useless-concat': 'error',
        },
    },
];
