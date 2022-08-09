import { writable } from "svelte/store";
import { browser } from "$app/env";
export const waitinglist = writable([]);


export let currentTicket = browser ? writable(JSON.parse(window.localStorage.getItem("currentTicket"))) : writable();

currentTicket.subscribe((value) => {
	if (browser && value) {
		window.localStorage.setItem("currentTicket", JSON.stringify(value)) 
	} 	
}) 

// export const fetchTicket = async () => {
//     //const url = `http://127.0.0.1:8000/queue/ticket/?called=False`; //?called=False ... ticket
// 	//const url = `http://127.0.0.1:8000/queue/ticket/?called=False`; 

// 	const url = `http://backend:8000/queue/ticket/?called=False`; 
// 	const res = await fetch(url);
// 	if (!res.ok) {
// 		throw new Error(`${res.status} ${res.statusText}`);
// 	}
// 	const data = await res.json();

// 	waitinglist.set(data);
// 	// set a timeout
// 	setTimeout(fetchTicket, 1000);
// }

// fetchTicket();

export default function (url) {
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



