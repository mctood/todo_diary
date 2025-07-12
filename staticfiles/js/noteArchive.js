function dateSelectors() {
	const monthSelector = $("#note-month-selector")
	const yearSelector = $("#note-year-selector")

	const dateUpdate = () => {
		let month = monthSelector.val()
		let year = yearSelector.val()

		location.href = `?month=${month}&year=${year}`
	}

	monthSelector.on('change', dateUpdate)

	yearSelector.on('change', dateUpdate)
}

$(() => {
	dateSelectors()
})