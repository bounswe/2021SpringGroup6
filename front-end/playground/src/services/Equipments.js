import axios from 'axios';

const localData = JSON.parse(localStorage.getItem('user')) || {};
const token = `Token ${localData.token}`;

export const createEquipmentDiscussion = async (equipmentId, text = 'text') => {

    return axios({
        method: 'POST',
        url: `/equipments/${equipmentId}/discussion`,
        headers: {
            Authorization: token,
        },
        data: {
            text,
        }
    })
        .then(response => {
            return response.data
        })
        .catch(error => {
            console.log(error)
        })
}
export const getEquipmentDiscussions = async (equipmentId) => {

    return axios({
        method: 'GET',
        url: `/equipments/${equipmentId}/discussion`,
        headers: {
            Authorization: token,
        },
    })
        .then(response => {
            return response.data
        })
        .catch(error => {
            console.log(error)
        })
}
