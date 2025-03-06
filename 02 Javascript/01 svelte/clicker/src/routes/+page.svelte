<script>
	import Timer from "$lib/components/Timer.svelte"
	import Upgrade from "$lib/components/Upgrade.svelte"
    import { multiplier } from "$lib/shared.svelte"

    let count = $state(0)
    let animPop = $state()
    let animBtn = $state()

    function increment() {
        count = count + multiplier.multi // multiplier["multi"]
        animBtn = "anim-btn"

        setTimeout(() => {
            animBtn = ""
        }, 100)

    }

    $effect(() => {
        if (count > 0) {
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


<div class="wrapper">
    <p class={animPop}>{count}</p>
    <button class="btn {animBtn}" onclick={increment}>Click me!</button>
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
        background-color: rebeccapurple;
        color: white;
    }

    .anim-btn {
        animation: btn-anim 0.1s;
    }

    .anim-pop {
        animation: popout 0.1s;
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