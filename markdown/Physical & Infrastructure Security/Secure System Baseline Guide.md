[Company Name]
Secure System Baseline Guide

**Document Version:** 1.0
**Date:** March 18, 2025

## 1. Overview

This Secure System Baseline Guide provides standard security configurations for systems and network devices used by [Company Name]. It aims to establish a minimum level of security for all IT resources and reduce the risk of security breaches. This is a *guide*, and specific configurations may need to be adjusted based on the specific hardware and software in use. The IT Support Provider is responsible for implementing and maintaining these baselines.

## 2. Purpose

The purpose of this guide is to:

*   Establish a consistent and secure configuration for all systems and devices.
*   Minimize vulnerabilities and reduce the attack surface.
*   Improve overall security posture.
*   Simplify system management and maintenance.
*   Provide a reference for configuring new systems and devices.

## 3. Scope

This guide applies to all systems and network devices owned, leased, or controlled by [Company Name], including:

*   **Windows Servers**
*   **Windows Workstations (Desktops and Laptops)**
*   **Network Devices (Routers, Switches, Firewalls)**
*   **Mobile Devices (Covered by MDM Policy)**

## 4. System Baselines

### 4.1. Windows Server Baseline

*   **Operating System:**
    *   Install the latest supported version of Windows Server.
    *   Apply all available security updates and patches (refer to Patch Management Policy).
    *   Enable automatic updates.
*   **Services:**
    *   Disable unnecessary services and features.
    *   Review running services regularly to ensure they are required.
*   **Accounts:**
    *   Rename the default Administrator account.
    *   Enforce strong password policies (refer to Password Policy).
    *   Use separate accounts for administrative tasks and regular user tasks.
    *   Disable or remove any unnecessary user accounts.
*   **Networking:**
    *   Enable Windows Firewall and configure it to block all unsolicited inbound traffic.
    *   Use secure protocols (e.g., RDP over VPN, HTTPS) for remote access.
*   **Auditing:**
    *   Enable auditing of logon/logoff events, account management events, and system events.
    *   Configure audit logs to be stored securely (refer to Log Management & Monitoring Policy).
*   **Security Software:**
    *   Install and maintain up-to-date antivirus/anti-malware software.
    *   Enable real-time protection.
*   **File System:**
    *  Use NTFS on all drives.
    *  Set appropriate permissions on files and folders.

### 4.2. Windows Workstation Baseline (Desktops and Laptops)

*   **Operating System:**
    *   Install the latest supported version of Windows.
    *   Apply all available security updates and patches (refer to Patch Management Policy).
    *   Enable automatic updates.
*   **Accounts:**
    *   Enforce strong password policies (refer to Password Policy).
    *   Use standard user accounts for daily tasks (avoid using administrator accounts for routine work).
*   **Networking:**
    *   Enable Windows Firewall and configure it to block all unsolicited inbound traffic.
    *   Use a VPN when connecting to company resources over public Wi-Fi (refer to Mobile Device Management Policy).
*   **Security Software:**
    *   Install and maintain up-to-date antivirus/anti-malware software.
    *   Enable real-time protection.
*   **Software Restrictions:**
    *   Restrict the installation of unauthorized software.
*   **Full Disk Encryption:**
     *  Enable Bitlocker (or similar full disk encryption).
*   **Screen Lock:**
     *  Enable automatic screen lock after 5 minutes of inactivity.

### 4.3. Network Device Baseline (Routers, Switches, Firewalls)

*   **Firmware:**
    *   Keep the device firmware up-to-date with the latest security patches.
*   **Default Passwords:**
    *   Change all default passwords to strong, unique passwords.
*   **Management Access:**
    *   Restrict management access to the device to authorized IP addresses.
    *   Use secure protocols (e.g., HTTPS, SSH) for management access.
    *   Disable unnecessary management interfaces (e.g., Telnet).
*   **Logging:**
    *   Enable logging of security-relevant events (refer to Log Management & Monitoring Policy).
    *   Configure logs to be sent to a central logging server (if available).
*   **Firewall Rules (for Firewalls):**
    *   Implement a "deny all" inbound policy, allowing only explicitly permitted traffic.
    *   Regularly review and update firewall rules.
*   **Wireless Security (for Wireless Routers/Access Points):**
    *   Use WPA2 or WPA3 encryption with a strong, unique password.
    *   Disable WPS (Wi-Fi Protected Setup).
    *   Change the default SSID (network name).
    *   Consider using a separate guest network for visitors.
* **Unused Ports:**
    * Disable any unused physical network ports on switches.

### 4.4 Mobile Devices
* Refer to Mobile Device Management (MDM) Policy.

## 5. Responsibilities

*   **IT Support Provider:** Is responsible for implementing and maintaining these secure system baselines.
*   **All Personnel:** Are responsible for adhering to these baselines and reporting any security concerns.

## 6. Revision History

| Version | Date       | Author      | Description of Change |
| :------ | :---------- | :---------- | :-------------------- |
| 1.0     | March 18, 2025 | Shijie Yin | Initial Guide Creation |
