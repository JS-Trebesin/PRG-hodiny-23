<script>
	import Timer from "$lib/components/Timer.svelte"

    let count = $state(0)
    let animPop = $state()
    let animBtn = $state()

    function increment() {
        count++
        animBtn = "anim-btn"

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
        animation: btn-anim 1s;
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