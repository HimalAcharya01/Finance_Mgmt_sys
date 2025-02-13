document.addEventListener("DOMContentLoaded", function () {
  fetch("/api/transaction/")  // Fetch data from Django API
      .then(response => response.json())
      .then(data => {
          const ctx = document.getElementById("myChart").getContext("2d");

          new Chart(ctx, {
              type: "doughnut", 
              data: {
                  labels: data.labels, 
                  datasets: [{
                      label: "Transaction Amount",
                      data: data.data,  
                      backgroundColor: [
                          "rgba(69, 60, 240, 0.6)",
                          "rgba(73, 80, 179, 0.6)",
                          "rgba(255, 206, 86, 0.6)",
                          "rgba(75, 192, 192, 0.6)",
                          "rgba(153, 102, 255, 0.6)",
                          "rgba(255, 159, 64, 0.6)"
                      ],
                      borderWidth: 1,
                      borderColor: 'transparent',  // Remove the border color
                      
                  }]
              },
              options: {
                  responsive: true,
                  maintainAspectRatio: false, 
                  plugins: {
                    legend: {
                        display: true,  // Set to false to hide labels
                        position: "bottom"
                    }
                }
              }
          });
      })
      .catch(error => console.error("Error fetching transaction data:", error));
});

