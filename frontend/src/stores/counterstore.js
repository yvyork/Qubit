import { writable } from 'svelte/store';
import { browser } from '$app/env';

export let counter = writable(
    browser && (localStorage.getItem('counter') || undefined)
)

counter.subscribe(id => {
    browser && (localStorage.counter = id);
})