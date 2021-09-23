<script>
	// import { authenticated } from "../stores/auth";
	// let auth = false;
	// authenticated.subscribe(auth => auth = a);



	import { page } from '$app/stores';
	const routes = [
		{ href: '/', name: 'Home' },
		{ href: '/registration', name: 'Registration' },
		{ href: '/login', name: 'Login' },
		{ href: '/contact', name: 'Contact Us' }
	];


	import {goto} from "$app/navigation"

    const logout = async () => {
        await fetch('http://localhost:8000/api/logout/', {
            method: 'POST',
            headers: {'Content-Type':'application/json'},
            credentials: 'include',
        });
        await goto("/")
    }
</script>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/css/all.min.css">
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css" >
	<!-- //web font -->
</head>
<nav class="navbar has-shadow is-fixed-top">
	<div class="navbar-menu">
		<a class:active={$page.path === '/userinfo'} class="navbar-item" sveltekit:prefetch href="/userinfo">My profile</a>
	</div>
    <a class="navbar-burger" id="burger">
        <span></span>
        <span></span>
        <span></span>
    </a>
    <div class="navbar-menu" id="nav-links">
        <div class="navbar-end">
			<!-- <div class="navbar-dropdown"> -->
		<!-- svelte-ignore a11y-missing-attribute -->
		
				
			<!-- </div> -->
	<!-- {#each routes as route}
		<a href={route.href}
            class="navbar-item is-dark"
			class:text-blue-300={route.href !== $page.path}
			class:text-gray-400={route.href === $page.path}>{route.name}</a
		> -->
		<a class:active={$page.path === '/'} class="navbar-item" sveltekit:prefetch href="/">Home</a>
		<a href="/" class="navbar-item" on:click={logout}>Logout</a>
		<a class:active={$page.path === '/registration'} class="navbar-item" sveltekit:prefetch href="/registration">Registration</a>
		<a class:active={$page.path === '/login'} class="navbar-item" sveltekit:prefetch href="/login">login</a>
</div>
</nav><br><br>

<!-- This is where the page will be rendered -->
<slot />
