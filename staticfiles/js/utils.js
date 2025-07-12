async function hashSHA256(message) {
	const textEncoder = new TextEncoder();
	const data = textEncoder.encode(message);
	const hashBuffer = await crypto.subtle.digest('SHA-256', data);
	const hashArray = Array.from(new Uint8Array(hashBuffer));
	return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

function startHashing() {
	let input = $("#hash-input")
	input.on('input', async () => {
		$('#hash-result').text(await hashSHA256(input.val().trim()))
	})
}

function getLineDimensions(element) {
    window.getSelection().selectAllChildren(element);

	let selection = window.getSelection();
	let range = selection.getRangeAt(0);
	return range.getClientRects();
}

async function wait(ms) {
	return new Promise((res) => {
		setTimeout(res, ms)
	})
}

$(() => {
	startHashing()

    $("[contenteditable]").on('input', function(){
        let element = $(this);
        if (!element.text().trim().length) {
            element.empty();
        }
    });
})