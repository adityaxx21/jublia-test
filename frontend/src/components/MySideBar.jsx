import { Sidebar } from "flowbite-react";
import {
  HiTable,
} from "react-icons/hi";

function MySideBar({ links }) {
  return (
    <Sidebar aria-label="Jublia Apps">
      <Sidebar.Items>
        <Sidebar.ItemGroup>
          {links.map((link) => (
            <Sidebar.Item href={link.to} icon={HiTable}>
              {link.text}
            </Sidebar.Item>
          ))}
        </Sidebar.ItemGroup>
      </Sidebar.Items>
    </Sidebar>
  );
}

export default MySideBar;
