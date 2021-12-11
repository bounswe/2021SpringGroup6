import {React, useState, Fragment} from 'react';
import {useNavigate} from 'react-router-dom';

function EventModal(props) {
    const navigate = useNavigate();
    function onDismiss() {
        navigate(-1);
    }

    return (<div onClick={onDismiss}>There is no discussion yet.</div>);
}

export {EventModal};