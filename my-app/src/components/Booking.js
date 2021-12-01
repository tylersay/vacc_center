import React, { useEffect, useState } from "react";
import axios from "axios";

const Booking = () => {
  const [vac_centers, setVac_Centers] = useState();
  const vac_center_url = "http://localhost:8000/api/vac_centers";

  useEffect(() => {
    const fetchVacCenter = async () => {
      const response = await axios.get(vac_center_url);
      const data = await response.data;
      setVac_Centers(data);
    };
    fetchVacCenter();
  }, []);

  return (
    <>
      <table>
        <thead>
          <tr>
            <th>Center Name</th>
            <th>Vaccine Type</th>
            <th>Postal Code</th>
          </tr>
        </thead>
        <tbody>
          {vac_centers.map((vac_center) => (
            <tr key={vac_center.id}>
              <td>{vac_center.center_name}</td>
              <td>{vac_center.vac_type}</td>
              <td>{vac_center.postal_code}</td>
              </tr>
          ))}
        </tbody>
      </table>
    </>
  );
};

export default Booking;
