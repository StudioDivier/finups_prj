// const tab = document.querySelectorAll('.info-header-tab');
// const info = document.querySelector('.info-header');
// const tabContent = document.querySelectorAll('.info-tabcontent');
//
// function hideTabContent(a) {
//     for (let i = a; i < tabContent.length; i++) {
//         tab[i].classList.remove('checked')
//
//         tabContent[i].classList.remove('show-tab');
//         tabContent[i].classList.add('hide-tab');
//     }
// }
//
// hideTabContent(1);
//
// function showTabContent(b) {
//     if (tabContent[b].classList.contains('hide-tab')) {
//         tab[b].classList.add('checked')
//
//         tabContent[b].classList.remove('hide-tab');
//         tabContent[b].classList.add('show-tab');
//     }
// }
//
// info.addEventListener('click', function (event) {
//     let target = event.target;
//     if (target && target.classList.contains('info-header-tab')) {
//         for (let i = 0; i < tab.length; i++) {
//             if (target == tab[i]) {
//                 hideTabContent(0);
//                 showTabContent(i);
//                 break;
//             }
//         }
//     }
// });
//
//
// const tab1 = document.querySelectorAll('.acc-header-tab');
// const info1 = document.querySelector('.acc-header');
// const tabContent1 = document.querySelectorAll('.acc-tabcontent');
//
// function hideTabContent1(a) {
//     for (let i = a; i < tabContent1.length; i++) {
//         tabContent1[i].classList.remove('show-tab');
//         tabContent1[i].classList.add('hide-tab');
//
//         tab1[i].classList.remove('a-up');
//         tab1[i].classList.add('a-down');
//
//         console.log(tabContent1)
//     }
// }
//
// hideTabContent1(1);
//
// function showTabContent1(b) {
//     if (tabContent1[b].classList.contains('hide-tab')) {
//         tabContent1[b].classList.remove('hide-tab');
//         tabContent1[b].classList.add('show-tab');
//
//         tab1[b].classList.add('a-up');
//         tab1[b].classList.remove('a-down');
//     }
// }
//
// info1.addEventListener('click', function (event) {
//     let target = event.target;
//     if (target && target.classList.contains('acc-header-tab')) {
//         for (let i = 0; i < tab1.length; i++) {
//             if (target == tab1[i]) {
//                 hideTabContent1(0);
//                 showTabContent1(i);
//                 break;
//             }
//         }
//     }
// });