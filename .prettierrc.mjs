export default {
    semi: true,
    tabWidth: 4,
    useTabs: false,
    printWidth: 100,
    singleQuote: true,

    plugins: [
        "prettier-plugin-css-order",
        "prettier-plugin-tailwindcss",
        // 
    ],

    overrides: [
        {
            files: '.github/**/*.yml',
            options: {
                tabWidth: 2,
            },
        },
    ],
};
