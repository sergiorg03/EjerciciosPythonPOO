feather.replace();

document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('tasksChart').getContext('2d');

    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Completadas', 'Pendientes'],
            datasets: [{
                data: window.tasksData, // usamos la variable global desde el template
                backgroundColor: [
                    'rgba(144, 240, 200, 0.7)', // Color completadas
                    'rgba(255, 99, 132, 0.7)'   // Color pendientes
                ],
                borderColor: [
                    'rgba(144, 240, 200, 1)',
                    'rgba(255, 99, 132, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        color: '#000' // o '#fff' si tu fondo es oscuro
                    }
                }
            }
        }
    });
});