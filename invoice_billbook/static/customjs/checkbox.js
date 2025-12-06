// Master checkbox select/deselect
document.addEventListener('DOMContentLoaded', function() {
    let selectAll = document.getElementById('select-all');
    if (selectAll) {
        // Master checkbox select/deselect
        selectAll.addEventListener('change', function() {
            let checked = this.checked;
            document.querySelectorAll('.row-checkbox').forEach(cb => cb.checked = checked);
        });

        // If all rows are selected manually, master checkbox also becomes checked
        document.querySelectorAll('.row-checkbox').forEach(cb => {
            cb.addEventListener('change', function() {
                let allChecked = document.querySelectorAll('.row-checkbox:checked').length === document.querySelectorAll('.row-checkbox').length;
                selectAll.checked = allChecked;
            });
        });
    }
});

