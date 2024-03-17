<template>
    <form id="cool-form" class="auth_form"> 

        <div id="name_field" class="input_field">
            <label for="name_field" class="input_name">User Name</label>

            <input 
                id="name-field-value" 
                placeholder=" " 
                type="text" required
                @input="inputName"
                :value="name">
        </div>

        <div id="email_field" class="input_field">
            <label for="email_field" class="input_name">Email</label>

            <input 
                id="email_field_value" 
                placeholder=" " 
                type="email" required
                @input="inputEmail"
                :value="email">
        </div>


        <div id="password_field" class="input_field">
            <label for="password_field" class="input_name">Password</label>

            <input 
                id="password_field_value" 
                placeholder=" " 
                required pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]){8,}$"
                @input="inputPassword"
                :value="password">

            <div class="password_info">
                <img src="../static/svg/info.svg" alt="info" class="password_info_img">

                <div id="password_instr" class="password_instr">
                    <ul>
                        <li>8 characters minimum</li>
                        <li> One lowercase character</li>
                        <li>One uppercase character</li>
                        <li>One number</li>
                    </ul>
                </div>
            </div>
        </div>

        <div id="agreement">
            <input id="agreement-value" type="checkbox" required>
            <label>Sign privacy and security agreement</label>
        </div>


        <div id="sign_up_btn" class="auth_btn" @click="submitForm">
            <button type="submit"> Sign up </button>
        </div>

    </form>
</template>

<script lang="ts">

export default{
    data(){
        return{
        name: '',
        email: '',
        password: '',
        agreement: ''
        }
    },

    methods:{
        submitForm() {
            
        },

        inputName(event){
            this.name = event.target.value
        },

        inputEmail(event){
            this.email = event.target.value
        },

        inputPassword(event){
            this.password = event.target.value
        }
    }
}
</script>



<style scoped>

@import url("../static/css/authForm.css");

.password_info{
    width: fit-content;
    position: absolute;
    left: 28%;
    top: 12%;
}
.password_info_img{
    opacity: .6;
    transition: opacity 0.05s;
    width: 20px;
}
.password_instr{
    display: none;
    position: relative;
    background-color: whitesmoke;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    border-radius: 25px;
    padding: 20px;
    bottom: 201px;
    left: 20px;
}
.password_instr ul{
    display: flex;
    flex-direction: column;
    gap: 9px;
    white-space: nowrap;
}
.password_info:hover .password_info_img{
    opacity: 0.9;
}
.password_info:hover .password_instr{
    display: block;

}


@media screen and (max-width: 600px){
    .password_info{
        left: 31%
    }
}
@media screen and (max-width: 400px){
    .password_info{
        left: 33%
    }
}
</style>