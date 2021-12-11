import {React, useState, Fragment} from 'react';
import {useNavigate, useParams} from "react-router-dom";

function DiscussionPage(props) {
    let navigate = useNavigate();
    let { id } = useParams();

    return (<div>There is no discussion yet.</div>);
}

export {DiscussionPage};