import { writable } from "svelte/store";
import { browser } from "$app/env";


export let currentTicket = browser ? writable(JSON.parse(window.localStorage.getItem("currentTicket"))) : writable();

currentTicket.subscribe((value) => {
	if (browser && value) {
		window.localStorage.setItem("currentTicket", JSON.stringify(value)) 
	} 	
}) 


export default function (url) {

	const waitinglist = writable([]);
	const loading = writable(false)
	const error = writable(false)

	async function get() {
		loading.set(true)
		error.set(false)
		try {
			const response = await fetch(url)
			waitinglist.set(await response.json())
		} catch(e) {
			error.set(e)
		}
		loading.set(false)
	}

	get()

	return [waitinglist, loading, error, get]
}



