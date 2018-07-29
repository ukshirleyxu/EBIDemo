<template>
    <Menu mode="horizontal" :theme="theme1" active-name="1">
        <a class="logo"><img src="/static/img/logo/biocontainers-logo.png" width="40" height="40">BioContainers Registry UI</a>
        <div class="menu">
            <MenuItem name="1">
                <Icon type="ios-home-outline"></Icon>
                BioContainers
            </MenuItem>
            <MenuItem name="2">
                <Icon type="social-github"></Icon>
                GitHub
            </MenuItem>
        </div>
    </Menu>
</template>
<script>
    export default {
        data () {
            return {
                
            }
        }
    }
</script>
<style scoped>
    .logo{
        float: left;
        color: #495060;
        text-decoration: none;
        display: flex;
        align-items: center;
        padding-left:10px;
        font-size: 16px;
        font-weight: bold;
    }
    .logo img{
        margin-right: 10px;
    }
    .menu{
        float: right;
    }
</style>


