<script>
    import {onMount} from "svelte";

    let username;
    // let user = { is_prouser: false };
    onMount(async () => {
        const response = await fetch("http://localhost:8000/api/user/", {
            headers: {'Content-Type':'application/json'},
            credentials: 'include',
        })

        const content = await response.json()
        // console.log(content)
        username =`${content.username}`;
    });


    import { page } from "$app/stores";
    import {goto} from "$app/navigation"


    export let id = $page.params.replace;
    let maf_file;
    const replace = async () => {
        const dataArray = new FormData();
        dataArray.append("username", username);
        dataArray.append("maf_file", maf_file[0]);
        await fetch(`http://localhost:8000/api/editfile/${id}/`, {
            
        method: "POST",
        // headers: {"Content-Type": "multipart/form-data"},
        credentials: "include",
        body: dataArray
    }).then((response) => response.json()).then((result) => {
            console.log('Success:', result);
        })
                .catch((error) => {
                    console.error('Error:', error);
                });
        await goto("/")
    }

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
            <form on:submit|preventDefault={replace} >
                <div class="columns is-centered mb-0">
                    <div class="column is-4">
                            <input type="hidden" class="input" name='username' bind:value={username} hidden>
                        <div class="column">
                            <!-- svelte-ignore a11y-label-has-associated-control -->
                            <label class="lable">Upload MAf file:</label>
                            <input bind:files={maf_file} type="file" name="maf_file" required="required">
                            <button class="button is-link" type="submit">Replace</button>                                
                        </div>
                    </div>
                </div>
            </form>
        </div>
        </div>
    </div>