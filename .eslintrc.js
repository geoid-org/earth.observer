module.exports = {
    root: true,
    rules: {
        semi: "error",
        "prefer-const": "error",
        "prettier/prettier": "error",
        "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
        "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
        "@typescript-eslint/no-unused-vars": "off",
        // "@typescript-eslint/no-unused-vars-experimental": "error",
        "no-unused-vars": "off"
    },
    env: {
        // browser: true,
        node: true
    },
    extends: [
        "plugin:vue/vue3-essential",
        // "eslint:recommended",
        "plugin:@typescript-eslint/eslint-recommended",
        "plugin:@typescript-eslint/recommended",
        "@vue/typescript/recommended",
        "plugin:prettier/recommended"
    ],
    parserOptions: {
        ecmaVersion: 2020
        // parser: 'babel-eslint'
    }
};
