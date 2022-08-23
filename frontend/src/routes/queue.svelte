
<script>
    import TicketList from '.././components/TicketList.svelte';  
	import ServingTicket from '../components/ServingTicket.svelte';
	import {currentTicket} from '../stores/ticketstore';
	import fetchStore from '../stores/ticketstore'

	let local = "127.0.0.1";
	let server = "10.65.15.141";


	let url = `http://127.0.0.1:8000/queue/ticket/?called=False`;

	const [data,loading,error,get] =fetchStore(url)
	setInterval(() => {
		get()
	}, 1000);


	const ticketAufruf = async (e) => {
		$currentTicket = e.detail;
		data.update((list) => {
			return (list || []).filter(t => t.id !== $currentTicket.id)
		});
		const url = `http://127.0.0.1:8000/queue/ticket/${$currentTicket.id}`;
		$currentTicket.called = true;
		const res = await fetch(url, {
			method: 'PUT',
			headers: { 'Content-Type': 'application/json'},
			body: JSON.stringify($currentTicket),  
		});


	}


</script>

<svelte:head>
	<title>Warteliste</title> 
</svelte:head>


<ServingTicket bind:$currentTicket/>
<hr id="ruler">
<h1 id="warteliste" class="text-4xl text-center my-8 uppercase"><strong>Warteliste</strong></h1>



{#if $error}
	<p>Error: {$error.message}</p>
{:else}
<div class="max-w-lg mx-auto"> 
	<TicketList list={data} on:aufrufen={ticketAufruf}/>
</div>
{/if}



<style>
	#warteliste {
		color: white;
	}

	#ruler {
		color: white;
	}
</style>