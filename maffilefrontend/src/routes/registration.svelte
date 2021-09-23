<script>
  
    import {onMount} from 'svelte'
  onMount(() => {
    let togglePassword = document.querySelector('#togglePassword');
    let passwordt = document.querySelector('#id_password');
  
  togglePassword.addEventListener('click', function (e) {
    // toggle the type attribute
    let type = passwordt.getAttribute('type') === 'password' ? 'text' : 'password';
    const icon = type == 'password' ? 'far fa-eye-slash' : 'far fa-eye'
    passwordt.setAttribute('type', type);
    // toggle the eye slash icon
    togglePassword.className = icon
  });
  
  const togglePassword1 = document.querySelector('#togglePassword1');
  const password1 = document.querySelector('#is_password');
  
  togglePassword1.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password1.getAttribute('type') === 'password' ? 'text' : 'password';
    const icon = type == 'password' ? 'far fa-eye-slash' : 'far fa-eye'
    password1.setAttribute('type', type);
    // toggle the eye slash icon
    togglePassword1.className = icon
  });
  });
  
  
  import {goto} from "$app/navigation"
  let username ='', email ='', password ='', password2 =''
  
  const submit = async () => {
    await fetch('http://localhost:8000/api/registration/', {
        method : 'POST',
        headers : {'content-type':'application/json'},
        body : JSON.stringify({
            username,
            email,
            password,
            password2
        })
    });
  
    await goto("/login")
  }
  
  
  </script>
  
  <div class="box">
  <div class="container">
  <div class="column is-4">
    <p class="panel-heading has-text-centered">
        Registration
      </p>
  <form on:submit|preventDefault={submit} class="box">
   <div class="field">
            <!-- svelte-ignore a11y-label-has-associated-control -->
            <label class="label">Username</label>
            <div class="control has-icons-left has-icons-right">
              <input class="input" bind:value={username} type="text" placeholder="Username" required="required">
              <span class="icon is-small is-left">
                <i class="fas fa-user"></i>
              </span>
            </div>
        </div>
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
    <div class="field">
        <!-- svelte-ignore a11y-label-has-associated-control -->
        <label class="label">Confirm password</label>
        <p class="control has-icons-left">
            <input bind:value={password2} class="input" id="is_password" type="password" name="password2" placeholder="Confirm password"  required="required">
            <i class="far fa-eye-slash" id="togglePassword1" ></i>
          <span class="icon is-small is-left">
            <i class="fas fa-lock"></i>
          </span>
        </p>
    </div>
    <div class="column is-fullwidth"><button class="button is-primary is-fullwidth">SIGNUP</button></div>
    <div>Already have an account? <a href="/login">Login here</a></div>
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
  /* far fa-eye-slash{
  margin-left: 50px;
  cursor: pointer;
  } */
  
  </style>
  