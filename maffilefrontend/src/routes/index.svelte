<script>

    // import id from './update.svelte'
    // // import { handleErrors } from "../shared.js";
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
        // console.log(content);       
    });


    // import {goto} from "$app/navigation"
    // import user from './data.svelte'

    // document.getElementById('upload').addEventListener('submit', function(event) {
    // event.preventDefault();
    // let input = document.getElementById('maf');


//   let files;
  let maf_file;
    
    function submit() {
        const dataArray = new FormData();
        dataArray.append("username", username);
        dataArray.append("maf_file", maf_file[0]);
        const submit = fetch("http://localhost:8000/api/maffileupload/", {
            
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
    }



    import { writable, derived } from 'svelte/store';
	export const apiData = writable([]);
	
	export const Data = derived(apiData, ($apiData) => {
	  if ($apiData.data){
		// return $apiData.data.map(username => username.username);
		return $apiData.data;
	  }
	  return [];
	});
    onMount(async () => {
        // const response = await fetch('http://127.0.0.1:8000/userview', {
        const response = await fetch('http://localhost:8000/api/usermaffiles/', {
        headers: {'Content-Type':'application/json'},
        credentials: 'include',
        })
        .then(response => response.json())
        .then(data => {
                console.log(data);
            apiData.set(data);
        }).catch(error => {
            console.log(error);
            return [];
        });
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
                <form>
                            <div class="columns is-centered mb-0">
                                <div class="column is-4">
                                    <input
                                    type="text"
                                    bind:value={username}
                                    placeholder="Name" name="username" hidden
                                  />
                                    <div class="column">
                                        <!-- svelte-ignore a11y-label-has-associated-control -->
                                        <label class="lable">Upload MAf file:</label>
                                        <input type="file" 
                                        bind:files={maf_file} name="maf_file" required="required">
                                        <button class="button is-link" type="submit" on:click|preventDefault={submit}>Upload</button>                                
                                    </div>
                                </div>
                            </div>
                </form>
            </div>
            </div>
        </div>

        <!-- <div>
            <form enctype="multipart/form-data">
              <input
                type="text"
                bind:value={username}
                placeholder="Name" name="username"
              />
              <br />
              <input 
                type="file" 
                bind:files={maf_file} name="maf_file"/>
              <br />
              <input on:click={submit} type="submit" />
            </form>
          </div> -->

        {#each $Data as data}
                <!-- <ul> -->
                    <div class="notification is-info">
                        <a href="{data.maf_file }">{data.maf_file}</a>
                        <a href={`/replace/${data.id}`}><button type="button">replace</button></a>
                    </div>
                <!-- </ul> -->
        {/each}