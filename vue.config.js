const path = require("path");
const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
    chainWebpack(config) {
        config.entry("app").clear().add("./src/main.ts").end();
        config.resolve.alias
            .set("~", path.join(__dirname, "./node_modules"))
            .set("@", path.join(__dirname, "./src"))
            .set("#", path.join(__dirname, "./src"));
    },
    transpileDependencies: true,
    css: {
        sourceMap: true,
        loaderOptions: {
            sass: {
                additionalData: `
                @import "@/assets/style/main.scss";
                `
            }
        }
    },
    assetsDir: "@/assets/"
});
