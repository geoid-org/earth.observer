<template>
    <div class="home">
        <img class="logo" alt="Vue logo" src="../assets/image/logo.png" />
        <HelloWorld msg="Welcome to Earth Observer" />
    </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import HelloWorld from "@/components/HelloWorld.vue"; // @ is an alias to /src

@Options({
    components: {
        HelloWorld
    }
})
export default class HomeView extends Vue {}
</script>

<style scoped>
.logo {
    width: 200px;
}
</style>
