document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    var infoPageURL = calendarEl.getAttribute('data-info-url');
    var selectedDateInput = document.getElementById('selectedDateInput');
    var csrfToken = "{{ csrf_token }}";
     
    var calendar = new FullCalendar.Calendar(calendarEl, {
        slotMinTime: '08:00:00',
        slotMaxTime: '24:00:00',
       
       
        slotLabelFormat: {
            hour: 'numeric',
            minute: '2-digit',
            omitZeroMinute: false,
            meridiem: 'short'
        },
        slotLabelInterval: { hour: 1 },
        slotLabelContent: function(arg) {
            
            var hour = arg.date.getHours(); // Saati al
            var minute = arg.date.getMinutes(); // Dakikayı al
    
            // Saati ve dakikayı iki basamaklı hale getir
            var formattedHour = hour.toString().padStart(2, '0');
            var formattedMinute = minute.toString().padStart(2, '0');
                
            // Özel bir saat etiketi oluştur (24 saat biçiminde)
            var customLabel = formattedHour + ':' + formattedMinute+'-' + (hour+1)+ ':' + formattedMinute;
    
            // Oluşturulan özel saat etiketini döndür
            return customLabel;
         },
    
        selectable: true,
        timeZone: 'UTC',
        initialView: 'timeGridSevenDay',
        headerToolbar: {
            left: 'prev,next',
            center: 'title',
            right: 'timeGridDay,timeGridSevenDay'
        },
        views: {
            timeGridSevenDay: {
                type:'timeGrid',
               
               
                duration: {
                    days: 7,
                     
                },
                buttonText: '7 day'
            }
        },
        dateClick: function (info) {
            focus();

            var selectedDate = info.dateStr;

            selectedDateInput.value = selectedDate;

        },
        
     
    });

    calendar.render();

    function focus() {
        
        var inputElement = document.getElementById('form');
        inputElement.focus();
    }

});
