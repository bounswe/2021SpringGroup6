import {React, useState, useEffect, useContext} from 'react';
import { Card } from 'react-bootstrap'
import './Badges.css';
import {UserContext} from '../../../../UserContext';
import axios from 'axios';
import SportNames from '../../../../PermanentComponents/SportNames.js';
import { Button, Input, Label,  UncontrolledCollapse, ButtonGroup } from 'reactstrap';

import {getUserInfo} from '../../../../services/User';

function Badges_Tab() {
    

    return (
    <div style={{minWidth: '45%', padding: '4rem 0', margin: 'auto'}}>
        <div style={{textAlign: 'center'}}>...</div>
    </div>
    )
}

export default Badges_Tab;
