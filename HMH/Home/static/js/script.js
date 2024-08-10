document.addEventListener('DOMContentLoaded', function() {
    const images = [
        '/static/images/maram.png',
        '/static/images/adrees.png',
        '/static/images/mohammed.jpg'
    ];
    
    const texts = [
        {
            title: 'dr.Halah amen',
            specialization: 'Obstetrics and Gynecology Specialist',
            details: `
                - performing natural obstetrics and repairing the perineum <br>
                - following up on pregnancy <br>
                - family planning <br>
                - following up on obstetrics and gynecology
            `
        },
        {
            title: 'dr.Adrees Ahmed',
            specialization: 'Internal Medicine Specialist',
            details: `
                - managing chronic diseases <br>
                - conducting general health assessments <br>
                - providing preventive care <br>
                - offering treatment for various medical conditions
            `
        },
        {
            title: 'dr.Mohammed Al-Farhan',
            specialization: 'Cardiology Specialist',
            details: `
                - diagnosing heart conditions <br>
                - providing cardiovascular treatment <br>
                - conducting stress tests <br>
                - offering lifestyle and preventive advice
            `
        }
    ];
    
    const imgElement = document.querySelector('.img-dr');
    const titleElement = document.querySelector('.box h4');
    const specializationElement = document.querySelector('.box h5');
    const detailsElement = document.querySelector('.box p');

    let currentIndex = 0;

    function changeContent() {
        imgElement.classList.add('fade'); 
        titleElement.classList.add('fade'); 
        specializationElement.classList.add('fade');
        detailsElement.classList.add('fade');

        setTimeout(() => {
            currentIndex = (currentIndex + 1) % images.length;
            imgElement.src = images[currentIndex];
            
           
            titleElement.innerHTML = texts[currentIndex].title;
            specializationElement.innerHTML = texts[currentIndex].specialization;
            detailsElement.innerHTML = texts[currentIndex].details;

            
            imgElement.classList.remove('fade');
            titleElement.classList.remove('fade');
            specializationElement.classList.remove('fade');
            detailsElement.classList.remove('fade');
        }, 1000); 
    }

    setInterval(changeContent, 5000); 
});
const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("animate");
        }
      });
    },
    { threshold: 0.5 }
  );
  
  const elements = document.querySelectorAll(".animate-on-scroll");
  elements.forEach((element) => {
    observer.observe(element);
  });
