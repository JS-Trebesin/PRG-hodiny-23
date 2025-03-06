<script>
    import { multiplier } from "$lib/shared.svelte"

    let shopClicked = $state(false)

    let { upgradeLevel } = $props()

    function upgradeShop() {
        shopClicked = !shopClicked

        if ( upgradeLevel === 1) {
            multiplier.multi = 2
        } else if ( upgradeLevel === 2) {
            multiplier.multi = 5
        } else if ( upgradeLevel === 3) {
            multiplier.multi = 10
        }
    }
</script>

<div>
    {#if shopClicked}
        <p>Shop upgraded</p>
    {:else}
        <p>Upgrade to level {upgradeLevel} shop</p>
    {/if}

    <button class="btn" onclick={upgradeShop}>Upgrade </button>
</div>


<style>
    .btn {
        border: 1px solid white;
        padding: 0.25em 0.5em;
        background-color: #00baa5;
        border-radius: 5px;
        color: white;

        transition: 0.5s linear;
    }

    .btn:active {
        scale: 0.5;
    }

    div {
        border: 2px solid #00baa5;
        padding: 0.5em 0.5em;
        margin: 5px;
        width: fit-content;
        border-radius: 5px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        gap: 10px;
    }
        
</style>