<script>
	import Timer from "$lib/components/Timer.svelte"
	import Upgrade from "$lib/components/Upgrade.svelte"
    import { shared } from "$lib/shared.svelte"

    
    let animPop = $state()
    let animBtn = $state()

    const colours = ["rebeccapurple", "deeppink", "Teal", "firebrick", "lime"]
    let selectedColour = $state(colours[0])

    function increment() {
        shared.count = shared.count + shared.multi // shared["multi"]
        animBtn = "anim-btn"

        setTimeout(() => {
            animBtn = ""
        }, 100)

    }

    $effect(() => {
        if (shared.count > 0) {
            animPop = "anim-pop"
        }

        setTimeout(() => {
            animPop = ""
        }, 100)
    })
</script>


<Timer />
<Upgrade upgradeLevel={1}/>
<Upgrade upgradeLevel={2}/>
<Upgrade upgradeLevel={3}/>

{#each colours as colour}
    <button class="circle" onclick={() => selectedColour = colour} aria-label={colour} style="--colour: {colour}"></button>
{/each}


<div class="wrapper">
    <p class={animPop}>{shared.count}</p>
    <button class="btn {animBtn}" onclick={increment} style="--colour: {selectedColour}">Click me!</button>
</div>


<style>
    
    .wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        min-height: 100vh;
        gap: 1em;
    }


    .btn {
        border: 2px solid black;
        padding: 1em 2em;
        border-radius: 5000px;
        background-color: var(--colour, rebeccapurple);
        color: white;
    }

    .anim-btn {
        animation: btn-anim 0.1s;
    }

    .anim-pop {
        animation: popout 0.1s;
    }

    .circle {
        aspect-ratio: 1/1;
        height: 50px;
        border-radius: 50%;
        background-color: var(--colour, lime);
        margin-inline: 2px;
    }

    @keyframes popout {
        50% {
            scale: 2;
        }

        100% {
            scale: 1;
        }
    }

    @keyframes btn-anim {
        100% {
            scale: 0.9;
        }
    }
</style>