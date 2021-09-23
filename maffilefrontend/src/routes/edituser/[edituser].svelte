<script>
    import { page } from "$app/stores";
    import {goto} from "$app/navigation"

    let email;
    export let username = $page.params.edituser;

    const editprofile = async () => {
            await fetch(`http://localhost:8000/api/editprofile/${username}/`, {
                method : 'PUT',
                method : 'POST',
                headers : {'content-type':'application/json'},
                credentials : 'include',
                body : JSON.stringify({
                   email,
                })
            });
            await goto("/maffile")
        };
</script>

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css" >
    <title>User Data</title>
    
</head>
<div class="cloumns">
    <div class="column">
        <div class="box" style="background-color: lightblue;">
            <form>
            <div class="columns is-centered mb-0">
                <div class="column-4">
                    <!-- svelte-ignore a11y-label-has-associated-control -->
                    <label class="lable">Username:</label>
                    <input bind:value={username} type="text" name="username" required="required" readonly>                               
                </div>
                <div class="column-4">
                    <!-- svelte-ignore a11y-label-has-associated-control -->
                    <label class="lable">Email:</label>
                    <input bind:value={email} type="text" name="email" required="required">                             
                </div>
                <div class="column-6">
                    <button type="button" on:click={editprofile}>Submit</button>                          
                </div>
            </div>
            </form>
        </div>
    </div>
</div>