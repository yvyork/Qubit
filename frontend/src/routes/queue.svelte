
<script>
    import TicketList from '.././components/TicketList.svelte';  
	import ServingTicket from '../components/ServingTicket.svelte';
	import {waitinglist, currentTicket} from '../stores/ticketstore'
	//import {currentTickets, waitinglist} from '../stores/ticketstore'
	import fetchStore from '../stores/ticketstore'


	let url = `http://127.0.0.1:8000/queue/ticket/?called=False`;

	const [data,loading,error,get] =fetchStore(url)


	const ticketAufruf = async (e) => {
		$currentTicket = e.detail;
		$waitinglist = $waitinglist.filter(t => t != $currentTicket)

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
	<!-- Vielleicht Schalter anstatt Warteliste -->
	<title>Warteliste</title> 
</svelte:head>


<ServingTicket bind:$currentTicket/>
<hr id="ruler">
<h1 id="warteliste" class="text-4xl text-center my-8 uppercase"><strong>Warteliste</strong></h1>


{#if $loading}
	<p>Loading...</p>
{:else if $error}
	<p>Error: {$error.message}</p>
{:else}
<div class="max-w-lg mx-auto"> 
	<TicketList on:aufrufen={ticketAufruf}/>
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