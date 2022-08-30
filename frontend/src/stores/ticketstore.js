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
			const data = await response.json();
			sortDataDirectly(data);
			waitinglist.set(data);
		} catch(e) {
			error.set(e)
		}
		loading.set(false)
	}

	get()

	return [waitinglist, loading, error, get]
}

function minutes(type, datestring) {
    return Math.round(type - (( Date.now() - datestring) / 60_000))
};

function sortDataDirectly(data) {
    data.sort((a,b) => {
        let Astring = Date.parse(a.timestamp);
        let Bstring = Date.parse(b.timestamp);
        let one = minutes(a.wait, Astring);
        let two = minutes(b.wait, Bstring); 
        let res = one - two;
        return res;
    });
}