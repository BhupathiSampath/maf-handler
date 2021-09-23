<script>
    import {onMount} from "svelte";

    let username;
    let email;
    // let user = { is_prouser: false };
    onMount(async () => {
        const response = await fetch("http://localhost:8000/api/user/", {
            headers: {'Content-Type':'application/json'},
            credentials: 'include',
        })

        const content = await response.json()
        // console.log(content)
        username =`${content.username}`,
        email = `${content.email}`;
        // console.log(content);       
    });
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
            <div class="columns is-centered mb-0">
                <div class="column-4">
                    <!-- svelte-ignore a11y-label-has-associated-control -->
                    <label class="lable">Username:</label>
                    <input bind:value={username} type="text" name="maf_file" required="required" readonly>                               
                </div>
                <div class="column-4">
                    <!-- svelte-ignore a11y-label-has-associated-control -->
                    <label class="lable">Email:</label>
                    <input bind:value={email} type="text" name="maf_file" required="required" readonly>                             
                </div>
                <div class="column-6">
                    <a href={`/edituser/${username}`}><button type="button">edit</button></a>                             
                </div>
            </div>
        </div>
    </div>
</div>
