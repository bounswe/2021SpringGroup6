import React from "react"
import {useParams} from "react-router-dom";
import EquipmentInformation from "./EquipmentInformation";



function EquipmentInformationFunctional(props) {
    const { id } = useParams();
    
    return (
        <div>
            <EquipmentInformation equipment_id={id} />
        </div>
    );
}

export default EquipmentInformationFunctional;