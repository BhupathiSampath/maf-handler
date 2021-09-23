<script>
    import {goto} from "$app/navigation"
    let email ='', password =''

    const submit = async () => {
        await fetch('http://localhost:8000/api/login/', {
            method: 'POST',
            headers: {'Content-Type':'application/json'},
            credentials: 'include',
            body: JSON.stringify({
                email,
                password
            }) 
        });
        await goto("/")
    }

    
</script>
<div class="box">
<div class="container">
    <div class="column is-4">
        <p class="panel-heading has-text-centered">
            Login here
          </p>
    <form on:submit|preventDefault={submit} class="box" style="margin-bottom: 10px; box-sizing: border-box;">
        <div class="field">
            <!-- svelte-ignore a11y-label-has-associated-control -->
            <label class="label">Email</label>
            <div class="control has-icons-left has-icons-right">
              <input bind:value={email} class="input" type="email" placeholder="Email" required="required">
              <span class="icon is-small is-left">
                <i class="fas fa-envelope"></i>
              </span>
            </div>
        </div>
        <div class="field">
            <!-- svelte-ignore a11y-label-has-associated-control -->
            <label class="label">Password</label>
            <p class="control has-icons-left">
                <input bind:value={password} class="input" id="id_password" type="password" name="password1" placeholder="Password"  required="required">
                <i class="far fa-eye-slash" id="togglePassword" ></i>
              <span class="icon is-small is-left">
                <i class="fas fa-lock"></i>
              </span>
            </p>
        </div> 
        <div class="column is-fullwidth"><button class="button is-primary is-fullwidth" type="submit">Sign in</button></div>
        <div>Don't have an account? <a href="/registration">Register</a></div>
    </form>
</div>
</div>
</div>


<style>
    .container {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    /* top: 200px; */
    /* bottom: 200px; */
    /* border-style:hidden; */
    /* border-style: double; */
    /* position: absolute; */
}
i{
    position: absolute;
    right: 15px;
    transform: translate(0,50%);
    top: 15%;
    cursor: pointer;
}
</style>
