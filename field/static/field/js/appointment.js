
document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    
    var selectedDateInput = document.getElementById('selectedDateInput');
    var csrfToken = "{{ csrf_token }}";
    var modal = document.getElementById('popupform');
    var span = document.getElementsByClassName("close")[0];
   
    var dateBlocks=document.querySelectorAll('.blockdate');





    var calendar = new FullCalendar.Calendar(calendarEl, {
        locale:'tr',
        slotMinTime: '08:00:00',
        slotMaxTime: '25:00:00',
        allDaySlot: false,
      
       
        slotLabelFormat: {
            hour: 'numeric',
            minute: '2-digit',
            omitZeroMinute: false,
            
        },
        slotDuration: { hour: 1 },
        
        
        slotLabelContent: function(arg) {
            
            var hour = arg.date.getHours(); 
            var minute = arg.date.getMinutes();
    
            
            var formattedHour = hour.toString().padStart(2, '0');
            var formattedMinute = minute.toString().padStart(2, '0');
                
           
            var customLabel = formattedHour + '.' + formattedMinute+'-' + ((hour + 1) === 24 ? "00" : (hour + 1)) + '.' + formattedMinute;
    
           
            return customLabel;
         },
    
        selectable: true,
        timeZone: 'Europe/Istanbul',
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
            openPopup()
           
            var selectedDate = info.dateStr;

            selectedDateInput.value = selectedDate;
            modal.style.display = 'block'; 
            info.el.classList.add('change-blok-click');

        },


        
     
     });

  

     function openPopup() {
        var modal = document.getElementById('popupform');
        modal.style.display = 'block';
        focus();
      }
    
      function closePopup() {
        var modal = document.getElementById('popupform');
        modal.style.display = 'none';
      }

      span.onclick = function() {
        var modal = document.getElementById('popupform');
        modal.style.display = "none";
    }

    reset.onclick = function() {
        var modal = document.getElementById('popupform');
        modal.style.display = "none";
    }
    submit.onclick = function() {
        var modal = document.getElementById('popupform');
        modal.style.display = "none";
        dateBlock.style.backgroundColor = 'red';
    }


    function focus() {
        
        var inputElement = document.getElementById('number');
        inputElement.focus();
    }



    // dateBlocks.forEach(function(dateBlock) {
    //     // Her tarih bloğunun tarihini alın (örneğin, data-date attribute kullanarak)
    //     var date = dateBlock.getAttribute('datedata');

    //     // Belirli bir koşula göre arka plan rengini değiştirin
    //     if (date === selectedDateInput) {
    //         dateBlock.style.backgroundColor = 'red'; // Örnek: Tarih 2023-10-19 ise kırmızı yap
    //     } else if (date === '2023-10-20') {
    //         dateBlock.style.backgroundColor = 'green'; // Örnek: Tarih 2023-10-20 ise yeşil yap
    //     }
    //     // Daha fazla koşul ekleyebilirsiniz.
    // });


    calendar.render();

});




document.addEventListener('DOMContentLoaded', function () {
    var calendarEl1 = document.getElementById('calendar1');
    var infoPageURL = calendarEl1.getAttribute('data-info-url');
    var selectedDateInput = document.getElementById('selectedDateInput1');
    var csrfToken = "{{ csrf_token }}";
    var modal1 = document.getElementById('popupform1');
    var span1 = document.getElementsByClassName("close1")[0];
    var forminfo1 = document.getElementById('forminfo1');




    var calendar1 = new FullCalendar.Calendar(calendarEl1, {
        locale:'tr',
        slotMinTime: '08:30:00',
        slotMaxTime: '25:30:00',
        allDaySlot: false,
      
       
        slotLabelFormat: {
            hour: 'numeric',
            minute: '2-digit',
            omitZeroMinute: false,
            
        },
        slotDuration: { hour: 1 },
        
        
        slotLabelContent: function(arg) {
            
            var hour = arg.date.getHours(); 
            var minute = arg.date.getMinutes();
    
            
            var formattedHour = hour.toString().padStart(2, '0');
            var formattedMinute = minute.toString().padStart(2, '0');
                
           
            var customLabel = formattedHour + '.' + formattedMinute+'-' + ((hour + 1) === 24 ? "00" : (hour + 1)) + '.' + formattedMinute;
    
           
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
            openPopup()
           
            var selectedDate1 = info.dateStr;

            selectedDateInput.value = selectedDate1;
            modal1.style.display = 'block'; 

        },


        
     
     });

  

     function openPopup() {
        var modal1 = document.getElementById('popupform1');
        modal1.style.display = 'block';
        focus();
      }
    
      function closePopup() {
        var modal1 = document.getElementById('popupform1');
        modal1.style.display = 'none';
      }

      span1.onclick = function() {
        var modal1 = document.getElementById('popupform1');
        modal1.style.display = "none";
    }

    reset1.onclick = function() {
        var modal1 = document.getElementById('popupform1');
        modal1.style.display = "none";
    }
    submit1.onclick = function() {
        var modal1 = document.getElementById('popupform1');
        modal1.style.display = "none";

    }


    function focus() {
        
        var inputElement = document.getElementById('number1');
        inputElement.focus();

    }



    calendar1.render();

});
