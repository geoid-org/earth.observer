module.exports = {
    root: true,
    rules: {
        semi: "error",
        "prefer-const": "error",
        "prettier/prettier": "error",
        "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
        "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off"
    },
    env: {
        // browser: true,
        node: true
    },
    extends: [
        "plugin:vue/vue3-essential",
        // "eslint:recommended",
        "@vue/typescript/recommended",
        "plugin:prettier/recommended"
    ],
    parserOptions: {
        ecmaVersion: 2020
        // parser: 'babel-eslint'
    }
};
